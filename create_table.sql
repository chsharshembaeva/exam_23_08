
CREATE TABLE payments
(
	ID SERIAL PRIMARY KEY
	Course_id INTEGER REFERENCES Courses(ID) ON DELETE CASCADE
	Amount NUMERIC(6,2)
	Pay_date DATE
	
)

(
    Id SERIAL PRIMARY KEY,
	FirstName CHARACTER VARYING(30) NOT NULL,
    CustomerId INTEGER DEFAULT 1,
    Quantity INTEGER,
	Phone VARCHAR(30) UNIQUE NOT NULL,
	TotalWeight NUMERIC(9,2),
    FOREIGN KEY (CustomerId) REFERENCES Customers (Id) ON DELETE SET DEFAULT
--  FOREIGN KEY (CustomerId) REFERENCES Customers (Id) ON DELETE CASCADE
-- 	FOREIGN KEY (CustomerId) REFERENCES Customers (Id) ON DELETE SET NULL
	PRIMARY KEY(OrderId, ProductId)
	UNIQUE(Email)
	UNIQUE(Phone) -- otdelno kajdiy
	UNIQUE(Email, Phone)  -- v svyazke vmeste budut unique
	CHECK((Age >0 AND Age<100) AND (Email !='') AND (Phone !=''))

);ProductId INTEGER NOT NULL REFERENCES Products(Id) ON DELETE CASCADE,