import os
import json
import re
"""Script that searches for the manifest.json files inside the behavior and resource pack folders
to then allow you to conviently manage the versions listed in the manifest.json files, and to
automatically sync the name to include the new version in the format vX.X.X"""

def find_folders(base_dir, keywords):
    matched_folders = []
    for root, dirs, files in os.walk(base_dir):
        for d in dirs:
            for keyword in keywords:
                if keyword.lower() in d.lower():
                    matched_folders.append(os.path.join(root, d))
                    break
    return matched_folders

def find_manifest_files(folders):
    manifest_files = []
    for folder in folders:
        manifest_path = os.path.join(folder, 'manifest.json')
        if os.path.isfile(manifest_path):
            manifest_files.append(manifest_path)
    return manifest_files

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json_string = json.dumps(data, indent=4)
        # Use regex to find and replace the multi-line lists
        json_string = re.sub(r'\[\s*(\d+),\s*(\d+),\s*(\d+)\s*\]', r'[\1, \2, \3]', json_string)
        file.write(json_string)

def check_versions(manifest_files):
    versions = []
    for file in manifest_files:
        data = read_json_file(file)
        version = tuple(data.get('header', {}).get('version', []))
        versions.append((file, version))
    return versions

def update_versions(manifest_files, new_version):
    new_version_list = [int(v) for v in new_version.split('.')]
    for file in manifest_files:
        data = read_json_file(file)
        if 'header' in data:
            data['header']['version'] = new_version_list
        if 'modules' in data:
            for module in data['modules']:
                module['version'] = new_version_list
        if 'dependencies' in data:
            for dependency in data['dependencies']:
                dependency['version'] = new_version_list
        write_json_file(file, data)

def update_name_with_version(manifest_files, new_version):
    for file in manifest_files:
        data = read_json_file(file)
        if 'header' in data:
            name = data['header'].get('name', '')
            if 'v' in name and any(char.isdigit() for char in name.split('v')[-1]):
                name = name.rsplit('v', 1)[0].strip()
            new_name = f"{name} v{new_version}"
            data['header']['name'] = new_name
            write_json_file(file, data)


def main():
    print("----Version update/sync tool for addon manifest.json files, by MRxSIR.----\n")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    behavior_keywords = ["behavior", "behavior_pack", " BP"]
    resource_keywords = ["resources", "resource_pack", "resource pack", " RP"]

    print("Searching for behavior pack folder in operating directory...")
    behavior_folders = find_folders(base_dir, behavior_keywords)
    if behavior_folders.__len__() > 1:
        print("Warning:  Multiple behavior pack folders found. Are you in a folder with multiple behavior packs?")
    
    print("Searching for resource pack folder in operating directory...")
    resource_folders = find_folders(base_dir, resource_keywords)
    if resource_folders.__len__() > 1:
        print("Warning:  Multiple resource pack folders found. Are you in a folder with multiple resource packs?")

    all_folders = behavior_folders + resource_folders
    manifest_files = find_manifest_files(all_folders)

    if not manifest_files:
        print("No manifest.json files found.")
        return
    else:
        print(f"Found {len(manifest_files)} manifest.json files.")

    versions = check_versions(manifest_files)
    version_set = set(version for _, version in versions)

    if len(version_set) > 1:
        print("Different versions found:")
        for file, version in versions:
            print(f"{file}: {version}")
    elif versions:
        for file, version in versions:
            print(f" - version {version}")


    print()
    update_choice = input("Do you want to set all versions to a new value? (yes/no): ").strip().lower()
    if update_choice == 'yes' or update_choice == 'y':
        new_version = input("Enter the new version (format: x.x.x): ").strip()
        update_versions(manifest_files, new_version)
        update_name_with_version(manifest_files, new_version)
        print(f"Versions and names updated.")
    else:
        print("Ok, no changes made.")
        if len(version_set) == 1:
            new_version = '.'.join(map(str, version_set.pop()))
            name_choice = input(f"Do you want to update the pack name to include the version {new_version}? (yes/no): ").strip().lower()
            if name_choice == 'yes':
                update_name_with_version(manifest_files, new_version)
                print("Names updated.")
            else:
                print("Ok, no changes made.")
        else:
            print("Versions are inconsistent and no changes were made.")

if __name__ == "__main__":
    main()
