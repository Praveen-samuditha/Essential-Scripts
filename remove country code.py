import openpyxl  # for Excel operations
import re  # for regular expressions

def remove_country_code(phone_number):
  """Removes country code from a phone number.

  Args:
      phone_number: The phone number string.

  Returns:
      The phone number without the country code (if found).
  """
  pattern = r"^\+[\d]{1,3}([-\.\s])?"  # Matches country code (+ and digits)
  match = re.match(pattern, phone_number)
  if match:
    return phone_number[match.end():]  # Remove matched part (country code)
  else:
    return phone_number  # No country code found, return as is

def process_phone_numbers(filename, output_filename):
  """Reads phone numbers from a text file, removes country codes, and writes them to an Excel sheet.

  Args:
      filename: The name of the text file containing phone numbers.
      output_filename: The name of the output Excel sheet.
  """
  # Open the text file for reading
  with open(filename, 'r') as file:
    phone_numbers = file.readlines()

  # Clean phone numbers (remove leading/trailing whitespaces)
  phone_numbers = [number.strip() for number in phone_numbers if number!= "\n"]

  # Remove country codes from phone numbers
  processed_numbers = [remove_country_code(number) for number in phone_numbers]

  # Create a new Excel workbook
  wb = openpyxl.Workbook()
  ws = wb.active
  ws.title = "Processed Phone Numbers"

  # Write the processed phone numbers to the first column (A)
  for row, number in enumerate(processed_numbers, start=1):
    ws.cell(row=row, column=1).value = number

  # Save the Excel workbook
  wb.save(output_filename)

# Get the filename from user input
filename = input("Enter the name of the text file containing phone numbers: ")

# Set the output filename (change "output.xlsx" if desired)
output_filename = "output.xlsx"

# Process and save the phone numbers
process_phone_numbers(filename, output_filename)

print(f"Phone numbers processed and saved to {output_filename}")
