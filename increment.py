import re

def increment_version_in_setup_file():
    with open('setup.py', 'r') as file:
        content = file.read()
        
        # Find the current version in the setup file
        version_match = re.search(r"version='(\d+\.\d+\.\d+)'", content)
        if version_match:
            current_version = version_match.group(1)
            major, minor, patch = map(int, current_version.split('.'))
            
            if minor == 9 and patch == 9:
                # If both minor and patch reach 9, increment the major component and set minor and patch to 0
                major += 1
                minor = 0
                patch = 0
            elif patch == 9:
                # If only patch reaches 9, increment the minor component and set patch to 0
                minor += 1
                patch = 0
            else:
                # Otherwise, increment the patch component by 1
                patch += 1
            
            # Construct the new version string
            new_version = f'{major}.{minor}.{patch}'
            
            # Replace the current version with the new version in the content
            updated_content = content.replace(current_version, new_version)
            
            # Write the updated content back to the setup file
            with open('setup.py', 'w') as updated_file:
                updated_file.write(updated_content)

# Call the function to increment the version in the setup file
increment_version_in_setup_file()
