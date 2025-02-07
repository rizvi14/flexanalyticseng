import json
from decimal import Decimal
from typing import Dict, List, Tuple

class FinancialDataValidator:
    def __init__(self, tolerance: Decimal = Decimal('0.01')):
        """Initialize validator with a tolerance level for floating point comparisons."""
        self.tolerance = tolerance
        self.validation_errors: List[str] = []
    
    def validate_node(self, node: Dict, path: str = '') -> Tuple[Decimal, bool]:
        """
        Recursively validate a node and its children.
        Returns (node_value, is_valid) tuple.
        """
        # Get the node's declared value
        declared_value = Decimal(str(node.get('value', '0')))
        
        # If there are no items, this is a leaf node
        if 'items' not in node:
            return declared_value, True
            
        # Calculate sum of children
        children_sum = Decimal('0')
        all_children_valid = True
        
        for child in node['items']:
            child_value, child_valid = self.validate_node(
                child, 
                f"{path}/{node.get('name', 'unnamed')}"
            )
            children_sum += child_value
            all_children_valid = all_children_valid and child_valid
        
        # Compare declared value with sum of children
        difference = abs(declared_value - children_sum)
        if difference > self.tolerance:
            error_msg = (
                f"Validation error at {path}/{node.get('name', 'unnamed')}: "
                f"Declared value ({declared_value}) differs from sum of "
                f"children ({children_sum}) by {difference}"
            )
            self.validation_errors.append(error_msg)
            return declared_value, False
            
        return declared_value, all_children_valid
    
    def validate_financial_data(self, data: Dict) -> bool:
        """
        Validate the entire financial data structure.
        Returns True if valid, False otherwise.
        """
        self.validation_errors = []
        
        # Validate each main section
        sections = ['assets', 'liabilities', 'equity']
        all_valid = True
        
        for section in sections:
            if section in data:
                _, section_valid = self.validate_node(data[section], f'/{section}')
                all_valid = all_valid and section_valid
        
        # Special validation: Assets = Liabilities + Equity
        if all(section in data for section in sections):
            assets_value = Decimal(str(data['assets']['value']))
            liabilities_value = Decimal(str(data['liabilities']['value']))
            equity_value = Decimal(str(data['equity']['value']))
            
            if abs(assets_value - (liabilities_value + equity_value)) > self.tolerance:
                error_msg = (
                    f"Balance sheet equation not satisfied: "
                    f"Assets ({assets_value}) ≠ "
                    f"Liabilities ({liabilities_value}) + "
                    f"Equity ({equity_value})"
                )
                self.validation_errors.append(error_msg)
                all_valid = False
        
        return all_valid

def validate_financial_json(json_data: str) -> Tuple[bool, List[str]]:
    """
    Validate a financial JSON string.
    Returns (is_valid, error_messages) tuple.
    """
    try:
        data = json.loads(json_data)
        validator = FinancialDataValidator()
        is_valid = validator.validate_financial_data(data)
        return is_valid, validator.validation_errors
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON format: {str(e)}"]
    except Exception as e:
        return False, [f"Validation error: {str(e)}"]

# Example usage
if __name__ == "__main__":
    # Read JSON data from a file
    with open('balancesheet.json', 'r') as f:
        json_data = f.read()
    
    # Validate the data
    is_valid, errors = validate_financial_json(json_data)
    
    # Print results
    print(f"Data validation {'passed' if is_valid else 'failed'}")
    if not is_valid:
        print("\nValidation errors:")
        for error in errors:
            print(f"- {error}")