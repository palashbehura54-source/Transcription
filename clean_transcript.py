# clean_transcript.py
# A simple script I put together to automate transcript cleaning for English data sets.
# It standardizes timestamps and makes sure acoustic tags are lowercase.

import os

def clean_text_data(input_file, output_file):
    print(f"Starting processing on: {input_file}")
    
    if not os.path.exists(input_file):
        print("Error: Input file not found. Please check the path.")
        return

    cleaned_lines = []
    
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            # Strip trailing whitespaces
            line = line.strip()
            
            if not line:
                continue  # skip empty lines
            
            # Simple human fix: make sure common AI tags are uniform/lowercase
            line = line.replace("[LAUGHTER]", "[laughter]")
            line = line.replace("[COUGH]", "[cough]")
            line = line.replace("[NOISE]", "[noise]")
            line = line.replace("[INAUDIBLE]", "[inaudible]")
            
            cleaned_lines.append(line)
            
    # Write the cleaned data to a new file
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for cleaned_line in cleaned_lines:
            out_file.write(cleaned_line + "\n")
            
    print(f"Done! Cleaned file saved to: {output_file}")

# Quick test run logic
if __name__ == "__main__":
    # Just a placeholder test setup
    test_input = "raw_transcript.txt"
    test_output = "cleaned_transcript.txt"
    
    # Create a quick fake file just to test if the logic works
    with open(test_input, "w") as f:
        f.write("[LAUGHTER] Hello this is a test. [NOISE]\n")
        f.write("We need to clean up [COUGH] these tags.\n")
        
    # Run the function
    clean_text_data(test_input, test_output)
