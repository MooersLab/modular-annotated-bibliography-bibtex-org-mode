import unittest
import os
import sys
from io import StringIO

# Import the functions from the script
from mdList2typList import format_citations, create_bib_notes_file

class TestCitationFormatting(unittest.TestCase):

    def test_format_citations(self):
        strings = ["Abdill2024HowToGuideForCodeSharingInBiology"]
        expected_output = [
            '=== #cite(label("Abdill2024HowToGuideForCodeSharingInBiology"), form: "full")\n#include "./bibNotes/Abdill2024HowToGuideForCodeSharingInBiology.typ"'
        ]
        self.assertEqual(format_citations(strings), expected_output)

    def test_create_bib_notes_file(self):
        test_string = "TestCitation"
        directory = "./bibNotes"
        file_path = os.path.join(directory, f"{test_string}.typ")

        # Ensure the directory and file do not exist before the test
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(directory):
            os.rmdir(directory)

        # Create the bib notes file
        create_bib_notes_file(test_string)

        # Check if the file was created
        self.assertTrue(os.path.exists(file_path))

        # Check if the content of the file is correct
        with open(file_path, 'r') as file:
            content = file.read().strip()
            self.assertEqual(content, "#include ../template.typ: *")

        # Clean up after the test
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(directory):
            os.rmdir(directory)

    def test_script_execution(self):
        input_filename = "test_input.md"
        output_filename = "test_output.typ"
        test_strings = ["Abdill2024HowToGuideForCodeSharingInBiology"]

        # Create a test input file
        with open(input_filename, 'w') as file:
            file.write("\n".join(test_strings))

        # Redirect stdout to capture print statements
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        # Execute the script
        sys.argv = ["mdList2typList.py", input_filename, output_filename]
        exec(open("mdList2typList.py").read())

        # Check the output file
        with open(output_filename, 'r') as file:
            output_content = file.read().strip()
            expected_output = '=== #cite(label("Abdill2024HowToGuideForCodeSharingInBiology"), form: "full")\n#include "./bibNotes/Abdill2024HowToGuideForCodeSharingInBiology.typ"'
            self.assertEqual(output_content, expected_output)

        # Clean up
        os.remove(input_filename)
        os.remove(output_filename)
        sys.stdout = original_stdout

if __name__ == '__main__':
    unittest.main()
