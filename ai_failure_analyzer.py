def analyze_failure(log):

    log = log.lower()

    if "modulenotfounderror" in log:
        return {
            "error_type": "Missing Python Module",
            "possible_cause": "A required Python package is missing.",
            "suggestion": "Check requirements.txt and install the missing package."
        }

    elif "assertionerror" in log:
        return {
            "error_type": "Test Failure",
            "possible_cause": "A test condition did not match the expected result.",
            "suggestion": "Check the failed test and compare the expected and actual values."
        }

    elif "syntaxerror" in log:
        return {
            "error_type": "Python Syntax Error",
            "possible_cause": "There is an invalid Python syntax in the source code.",
            "suggestion": "Check the line mentioned in the error and correct the Python syntax."
        }

    elif "docker" in log and "not recognized" in log:
        return {
            "error_type": "Docker Command Error",
            "possible_cause": "Jenkins cannot access the Docker executable.",
            "suggestion": "Check the Docker installation path and Jenkins environment configuration."
        }

    elif "docker build" in log and "failed" in log:
        return {
            "error_type": "Docker Build Failure",
            "possible_cause": "The Docker image could not be built successfully.",
            "suggestion": "Check the Dockerfile, dependencies, and Docker build logs."
        }

    else:
        return {
            "error_type": "Unknown Build Failure",
            "possible_cause": "The pipeline encountered an error that was not recognized.",
            "suggestion": "Review the Jenkins console log for the exact error message."
        }