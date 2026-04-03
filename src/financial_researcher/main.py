#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from financial_researcher.crew import FinancialResearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the financial researcher crew with the specified inputs.
    """
    inputs = {
        'company': 'Tesla',
    }

   
    result=FinancialResearcher().crew().kickoff(inputs=inputs)

    
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")


if __name__ == "__main__":
    run()
