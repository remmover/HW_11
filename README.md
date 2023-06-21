# Address Book

This is a simple command-line address book program written in Python. It allows you to store and manage contacts with their names, phone numbers, and optional birthdays. You can add new contacts, change phone numbers of existing contacts, retrieve phone numbers for specific contacts, and display all the contacts stored in the address book.

## Getting Started

To use the program, follow these steps:

1. Clone the repository or download the source code files.
2. Make sure you have Python 3 installed on your machine.
3. Run the program by executing the following command:

   ```
   python address_book.py
   ```

## Usage

Once the program is running, you can interact with it by typing commands into the console. Here are the available commands:

- `hello`: Displays a greeting message from the program.
- `add [Name] [Phone] [Birthday]`: Adds a new contact to the address book. The name and phone number are required, and the birthday is optional. Example: `add John Doe +380123456789 01.01.1990`
- `change [Name] [Phone]`: Changes the phone number of an existing contact. Example: `change John Doe +380987654321`
- `phone [Name]`: Retrieves the phone number(s) of a specific contact. Example: `phone John Doe`
- `show all [Count]`: Displays all the contacts stored in the address book. The optional `Count` parameter limits the number of contacts shown per page. Example: `show all 5`
- `help`: Displays a help message with the list of available commands.
- `good bye`, `close`, `exit`: Exits the program.

## Examples

Here are some examples of how to use the program:

```
> hello
Hello, how can I help you?

> add John Doe +380123456789 01.01.1990
You have added a contact with name: John Doe, phone number: +380123456789, and birthday: 01.01.1990

> change John Doe +380987654321
You have changed the phone number to +380987654321 in the contact with the name: John Doe

> phone John Doe
John Doe: num = +380987654321

> show all
{'John Doe': num = +380987654321}

> help
"hello", responds with "Hello, how can I help you?"
"add ...": Adds a new contact to the address book.
"change ...": Changes the phone number of an existing contact.
"phone ...": Retrieves the phone number(s) for a specific contact.
"show all": Displays all the contacts stored in the address book.
"good bye", "close", "exit": Exits the program.

> exit
Good bye!
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
