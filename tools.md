## Available Tools and Usage Instructions

### File Management Tools

*   **Write:** Create a new file or overwrite an existing one.
    *   Usage: `tool_code.write_file(path='<file_path>', content='<file_content>')`
*   **Read:** Read the content of a file.
    *   Usage: `tool_code.read_file(path='<file_path>')`
*   **Edit:** Add content to an existing file.
    *   Usage: `tool_code.append_file(path='<file_path>', content='<content_to_add>')`
*   **Modify:** Replace specific content within a file.
    *   Usage: `tool_code.replace_in_file(path='<file_path>', old_content='<old_text>', new_content='<new_text>')`
*   **Delete:** Delete a file.
    *   Usage: `tool_code.delete_file(path='<file_path>')`
*   **List Directory:** List the contents of a directory.
    *   Usage: `tool_code.list_directory(path='<directory_path>')`
*   **Save Version:** Copy a project to a backup location.
    *   Usage: `tool_code.save_version(source_path='<source_path>', destination_path='<destination_path>')`
*   **Restore Version:** Revert a project from a backup.
    *   Usage: `tool_code.restore_version(source_path='<source_path>', destination_path='<destination_path>')`
*   **Read Folder:** Read all files within a folder (bulk reading).
    *   Usage: `tool_code.read_folder(path='<folder_path>')`
*   **Ignore File:** Remove a file from the system's context (for the agent).
    *   Usage: `tool_code.ignore_file(path='<file_path>')`
*   **Ignore Folder:** Remove a folder from the system's context (for the agent).
    *   Usage: `tool_code.ignore_folder(path='<folder_path>')`
*   **Remove File:** Remove a file from the agent's current working context.
    *   Usage: `tool_code.remove_from_context(path='<file_path>')`
*   **Remove Folder:** Remove a folder from the agent's current working context.
    *   Usage: `tool_code.remove_folder_from_context(path='<folder_path>')`
*   **View Context:** View remaining tokens and list of files in the current context.
    *   Usage: `tool_code.view_context()`

### Other Tools

*   **Internet:** Access the internet for information gathering.
    *   Usage: `tool_code.internet_search(query='<search_query>')`
*   **Terminal Integration:** Execute shell commands.
    *   Usage: `tool_code.execute_terminal_command(command='<shell_command>')`
*   **Finish Task:** Signal completion of the current task and readiness for the next step in the workflow.
    *   Usage: `tool_code.finish_task()`

**Note:** The `tool_code` prefix is a placeholder. The actual implementation will depend on how the `ToolManager` exposes these functionalities to the agents. Agents should assume these functions are available in their environment.

