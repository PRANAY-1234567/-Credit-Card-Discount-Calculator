# 💳 Credit Card Discount Calculator

## 📌 Description

This Python program calculates a **10% discount** for customers who meet all of the following conditions:

* Payment mode must be **Credit Card**
* Customer must purchase **at least 3 products**
* Each product must cost **₹500 or more**

If all conditions are satisfied, the program calculates the total price and applies a **10% discount**.

## 🧠 Logic

The program checks the conditions step by step:

```text
Payment Mode
     ↓
Credit Card?
  ↓ Yes
Number of Products ≥ 3?
  ↓ Yes
Each Product Price ≥ ₹500?
  ↓ Yes
Calculate Total
     ↓
Apply 10% Discount
     ↓
Display Final Amount
```

## 💻 Technologies Used

* **Python**
* Conditional Statements (`if`, `else`)
* User Input
* Arithmetic Operators
* f-strings

## ⚙️ Conditions

| Condition             | Requirement |
| --------------------- | ----------- |
| Payment Mode          | Credit Card |
| Minimum Products      | 3           |
| Minimum Price/Product | ₹500        |
| Discount              | 10%         |

## 🧮 Example

### Input

```text
enter the Payment--mode "credit-card"
enter the Product Number 3
enter the Price 1000
enter the Price 800
enter the Price 600
```

### Calculation

```text
Total = 1000 + 800 + 600
      = ₹2400

Discount = 10% of ₹2400
         = ₹240

Final Amount = ₹2400 - ₹240
             = ₹2160
```

### Output

```text
Total amount is 2400 and discount amount is 2160
```

## ❌ When Discount Is Not Applied

### Example 1: Less than 3 products

```text
Product Number = 2
```

Output:

```text
less than 3 Product
```

### Example 2: Product price below ₹500

```text
P1 = 1000
P2 = 800
P3 = 400
```

Output:

```text
Product price is less than 500
```

### Example 3: Payment is not Credit Card

```text
Payment Mode = Cash
```

Output:

```text
Cash -----> 💷
```

## 📚 Concepts Learned

This program demonstrates:

1. `input()` for taking user input
2. `eval()` for converting input into Python values
3. Nested `if-else` statements
4. Comparison operators such as `>=`
5. Arithmetic calculations
6. Percentage/discount calculation
7. f-strings for formatted output

## 🚀 Future Improvements

The program can be improved by:

* Using `input()` with `int()`/`float()` instead of `eval()`
* Allowing the user to enter any number of products
* Calculating the discount using a separate function
* Adding multiple payment methods
* Adding different discount percentages
* Handling invalid user input

## 👨‍💻 Author

**Pranay Vishwanath Jadhao**

> A beginner Python program demonstrating conditional statements, nested conditions, and basic billing calculations.

