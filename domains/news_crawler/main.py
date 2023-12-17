import csv
import os
from typing import Any

from get_links import (DKNNewsLink, LuatKhoaLink, NgoisaoLink,
                       ThanhNienNewsLinks, VnExpressNewsLink, VTVNewsLinks)


class LinkCrawler:
    def __init__(self, sources) -> None:
        self.sources = sources

    def __call__(self) -> Any:
        for source in self.sources:
            crawler = source()
            crawler.get_articles_link().to_csv()
    

class CombineCSV:
    def __init__(self, directory_path, output_file) -> None:
        self.directory_path = directory_path
        self.output_file = output_file

    def __call__(self):
        # Get a list of all CSV files in the directory
        csv_files = [file for file in os.listdir(self.directory_path) if file.endswith('.csv')]

        # Check if there are any CSV files in the directory
        if not csv_files:
            print("No CSV files found in the specified directory.")
            return

        # Open the output file in write mode
        with open(self.output_file, 'w', newline='') as combined_csv:
            # Create a CSV writer object
            csv_writer = csv.writer(combined_csv)

            # Write the header (assuming the first file has the header)
            with open(os.path.join(self.directory_path, csv_files[0]), 'r') as first_file:
                header = next(csv.reader(first_file))
                csv_writer.writerow(header)

            # Loop through each CSV file and append its data to the combined CSV file
            for csv_file in csv_files:
                file_path = os.path.join(self.directory_path, csv_file)
                with open(file_path, 'r') as current_file:
                    # Skip the header in the current file
                    next(current_file)
                    # Write the remaining rows to the combined CSV file
                    for row in csv.reader(current_file):
                        csv_writer.writerow(row)

        print(f"Combined data saved to {self.output_file}")



link_crawler = LinkCrawler(sources=[
                                    VTVNewsLinks, 
                                    ThanhNienNewsLinks, 
                                    VnExpressNewsLink, 
                                    NgoisaoLink, 
                                    DKNNewsLink,
                                    LuatKhoaLink
                                    ])()


# Specify the directory containing CSV files and the output file name
directory_path = "/home/tomato/Desktop/Graduation_thesis/News-Verification-ML-Service/domains/news_crawler/links"
output_file = "/home/tomato/Desktop/Graduation_thesis/News-Verification-ML-Service/domains/news_crawler/links/combined_data.csv"

# Call the function to combine CSV files
CombineCSV(directory_path=directory_path, output_file=output_file)()
