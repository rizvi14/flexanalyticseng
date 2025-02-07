-- Create Categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER,
    name TEXT,
    value REAL
);

-- Create Subcategories table
CREATE TABLE IF NOT EXISTS subcategories (
    subcategory_id INTEGER,
    category_id INTEGER,
    name TEXT,
    value REAL,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Create Groups table
CREATE TABLE IF NOT EXISTS groups (
    group_id INTEGER,
    subcategory_id INTEGER,
    name TEXT,
    value REAL,
    FOREIGN KEY (subcategory_id) REFERENCES subcategories(subcategory_id)
);

-- Create Accounts table
CREATE TABLE IF NOT EXISTS accounts (
    account_id TEXT,
    group_id INTEGER,
    subcategory_id INTEGER,
    category_id INTEGER,
    name TEXT,
    value REAL,
    FOREIGN KEY (group_id) REFERENCES groups(group_id),
    FOREIGN KEY (subcategory_id) REFERENCES subcategories(subcategory_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Insert top-level categories
INSERT INTO categories (category_id, name, value) VALUES
    (1, 'ASSETS', 13318970.87),
    (2, 'Liabilities', 1025016.99),
    (3, 'Equity', 12399101.55);

-- Insert Asset subcategories
INSERT INTO subcategories (subcategory_id, category_id, name, value) VALUES
    (1, 1, 'Current Assets', 13300233.24),
    (2, 1, 'Fixed Assets', 18737.63);

-- Insert Asset groups
INSERT INTO groups (group_id, subcategory_id, name, value) VALUES
    (1, 1, 'Bank Accounts', -513160.89),
    (2, 1, 'Accounts Receivable', 13788410.16),
    (3, 1, 'Other Current Assets', 24983.97),
    (4, 2, 'Property, Plant, and Equipment', 18737.63);

-- Insert Asset accounts
INSERT INTO accounts (account_id, group_id, name, value) VALUES
    ('6c9790a2-0800-46cc-8c50-e29e69d8015c', 1, 'Flex Cash', 806291.61),
    ('b58e60f6-fe20-451e-9fc2-87eb58bcb297', 1, 'Flex Checking', -1272375.00),
    ('c7a7a89e-cc40-40b0-90dd-60f0dadedc41', 1, 'Flex 2761', -47077.50),
    ('bdd4df93-54ac-420c-8a9b-897a24f79c9c', 2, 'Accounts Receivable', 13788410.16),
    ('15560eaa-78c3-4ef6-bcc2-4697c9f509ef', 3, 'Payments to Deposit', 10000.00),
    ('1d09f6de-b8e5-4865-94e4-5a1f15e0ce04', 3, 'Prepaid Expenses', 14983.97),
    ('47c124b7-efcb-4225-95b8-7b85e2dcb977', 4, 'Office Equipment', 14855.91),
    ('3073b7ee-8d38-48e8-b2cc-a422ffb2d20f', 4, 'Furniture', 1017.08),
    ('6450bea2-bafc-40a5-9faa-0a069669f758', 4, 'Computers and Accessories', 2864.64);

-- Insert Liability subcategories
INSERT INTO subcategories (subcategory_id, category_id, name, value) VALUES
    (5, 2, 'Current Liabilities', 1014525.75),
    (6, 2, 'Long-Term Liabilities', 10491.24);

-- Insert Liability groups
INSERT INTO groups (group_id, subcategory_id, name, value) VALUES
    (7, 5, 'Accounts Payable', 83086.72),
    (8, 5, 'Credit Cards', 854440.93);

-- Insert Liability accounts
INSERT INTO accounts (account_id, group_id, name, value) VALUES
    ('09342b42-bfa9-459c-997b-f7dac52d32a6', 7, 'Accrued Rent', 69723.08),
    ('1cf73166-6064-4e55-875a-ede915e5f0cb', 7, 'Payable to Character', 9313.64),
    ('51818eb7-9561-4f26-8285-b391b90b3c21', 7, 'Accounts Payable', 4050.00),
    ('420851e1-e6f4-4f2f-9a15-3634fa24bce0', 8, 'Flex Bronze Card', 5817.50),
    ('1a6c59d8-ae89-4704-b6ec-721da2e6b7c0', 8, 'Flex Silver Card', 797087.28),
    ('6112362b-0dac-4172-a3da-5c89e4487768', 8, 'Flex Gold Card', 76536.15),
    ('fc38e9a5-f2f5-45b0-8466-ecfc36d28561', 8, 'Flex Platinum Card', -25000.00),
    ('220', 6, 'Settle Loans Payable', 10491.24);

-- Insert Equity subcategories
INSERT INTO subcategories (subcategory_id, category_id, name, value) VALUES
    (7, 3, 'Owners Equity', -95000.00);

-- Insert Equity accounts
INSERT INTO accounts (account_id, subcategory_id, name, value) VALUES
    ('831b6852-6f82-4ce1-b07b-88601d16457d', 7, 'Owners Equity', -95000.00),
    ('b1ba5fb3-5d54-4806-ad8d-e78bd2187e13', null, 'Retained Earnings', 11881707.50),
    ('49862dbf-e470-479e-98ae-c1e172bd86a3', null, 'Balance Adjustments', 122453.09);