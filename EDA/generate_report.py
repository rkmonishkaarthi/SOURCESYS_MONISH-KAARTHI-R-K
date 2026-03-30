import os
import pandas as pd
from google import genai
from prompts import get_data_cleaning_prompt

def main():
    # Verify the API key is set
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("Error: Please set your GEMINI_API_KEY environment variable.")
        print("Example (Windows Command Prompt): set GEMINI_API_KEY=your_key_here")
        print("Example (PowerShell): $env:GEMINI_API_KEY=\"your_key_here\"")
        return
        
    dataset_path = 'ecommerce_sales_data.csv'
    
    print(f"Loading dataset from {dataset_path}...")
    try:
        df = pd.read_csv(dataset_path)
    except Exception as e:
        print(f"Failed to load dataset: {e}")
        return
        
    # Get a descriptive sample of the data to send to Gemini
    # Converting the first 10 rows to a CSV string gives the model column names and example values
    print("Preparing data sample for the prompt...")
    sample_data = df.head(10).to_csv(index=False)
    
    # Build the prompt using the function you provided
    prompt = get_data_cleaning_prompt(sample_data)
    
    print("Sending request to Gemini API (gemini-2.5-flash)...")
    try:
        # Initialize the client from the new SDK
        client = genai.Client(api_key=api_key)
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        report_text = response.text
        
        # Save the generated response to a markdown report
        report_filename = "eda_cleaning_report.md"
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write("# Data Cleaning Report\n\n")
            f.write(f"Based on `{dataset_path}` (Total Rows: {len(df)})\n\n")
            f.write(report_text)
            
        print(f"\nSuccess! The report has been generated and saved to {report_filename}")
        print("\nHere is a preview of your report:\n")
        print("-" * 50)
        print(report_text)
        print("-" * 50)
        
    except Exception as e:
        print(f"Error during API call: {e}")

if __name__ == "__main__":
    main()
