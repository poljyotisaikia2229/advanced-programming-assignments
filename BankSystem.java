import java.util.*;


// Base Class: Account

class Account {
    private String accountNumber;
    private String ownerName;
    private double balance;

    // Default Constructor (Constructor Chaining)
    public Account() {
        this("0000", "Unknown", 0.0);
    }

    // Parameterized Constructor
    public Account(String accountNumber, String ownerName, double balance) {
        this.accountNumber = accountNumber;
        this.ownerName = ownerName;
        setBalance(balance); // validation through setter
    }

    // Getters and Setters (Encapsulation)
    public String getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(String accountNumber) {
        if (accountNumber == null || accountNumber.isEmpty())
            throw new IllegalArgumentException("Invalid account number");
        this.accountNumber = accountNumber;
    }

    public String getOwnerName() {
        return ownerName;
    }

    public void setOwnerName(String ownerName) {
        if (ownerName == null || ownerName.isEmpty())
            throw new IllegalArgumentException("Invalid owner name");
        this.ownerName = ownerName;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        if (balance < 0)
            throw new IllegalArgumentException("Balance cannot be negative");
        this.balance = balance;
    }

    // Deposit Method
    public void deposit(double amount) {
        if (amount <= 0)
            throw new IllegalArgumentException("Deposit must be positive");
        balance += amount;
    }

    // Withdraw Method
    public void withdraw(double amount) {
        if (amount <= 0)
            throw new IllegalArgumentException("Withdrawal must be positive");

        if (amount > balance)
            throw new IllegalArgumentException("Insufficient balance");

        balance -= amount;
    }

    // Display Method
    public void display() {
        System.out.println("Account No   : " + accountNumber);
        System.out.println("Owner Name   : " + ownerName);
        System.out.println("Balance      : " + balance);
    }
}


// Derived Class: SavingsAccount

class SavingsAccount extends Account {
    private double interestRate;

    public SavingsAccount(String accNo, String owner, double balance, double interestRate) {
        super(accNo, owner, balance); // constructor chaining
        this.interestRate = interestRate;
    }

    // Calculate Interest
    public double calculateInterest() {
        return getBalance() * interestRate / 100;
    }

    // Override display()
    @Override
    public void display() {
        System.out.println("\n--- Savings Account ---");
        super.display();
        System.out.println("Interest Rate: " + interestRate + "%");
        System.out.println("Interest     : " + calculateInterest());
    }
}


// Derived Class: CurrentAccount

class CurrentAccount extends Account {
    private double overdraftLimit;

    public CurrentAccount(String accNo, String owner, double balance, double overdraftLimit) {
        super(accNo, owner, balance);
        this.overdraftLimit = overdraftLimit;
    }

    // Override withdraw() with overdraft feature
    @Override
    public void withdraw(double amount) {
        if (amount <= 0)
            throw new IllegalArgumentException("Withdrawal must be positive");

        if (amount > getBalance() + overdraftLimit)
            throw new IllegalArgumentException("Overdraft limit exceeded");

        setBalance(getBalance() - amount);
    }

    // Override display()
    @Override
    public void display() {
        System.out.println("\n--- Current Account ---");
        super.display();
        System.out.println("Overdraft Limit: " + overdraftLimit);
    }
}


// Main Class

public class BankSystem {
    public static void main(String[] args) {

        // Polymorphism: Using base class reference
        List<Account> accounts = new ArrayList<>();

        accounts.add(new SavingsAccount("S001", "Alice", 1000, 5));
        accounts.add(new CurrentAccount("C001", "Bob", 500, 1000));

        // Display all accounts
        for (Account acc : accounts) {
            acc.display(); // dynamic binding
        }

        // Validation Test
        System.out.println("\n--- Transaction Test ---");
        try {
            accounts.get(0).withdraw(5000); // should fail
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}