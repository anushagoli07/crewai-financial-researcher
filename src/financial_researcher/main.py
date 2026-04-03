#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from financial_researcher.crew import FinancialResearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    inputs = {
        'topic': 'AI LLMs',
        'company': 'NVIDIA',
        'current_year': str(datetime.now().year)
    }
    try:
        FinancialResearcher().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    inputs = {
        'topic': 'AI LLMs',
        'company': 'NVIDIA',
        'current_year': str(datetime.now().year)
    }
    try:
        FinancialResearcher().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    try:
        FinancialResearcher().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    inputs = {
        'topic': 'AI LLMs',
        'company': 'NVIDIA',
        'current_year': str(datetime.now().year)
    }
    try:
        FinancialResearcher().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
