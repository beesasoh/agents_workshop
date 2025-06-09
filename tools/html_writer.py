import os
from agents import function_tool


@function_tool
def write_html_to_file(html_content: str, filename: str = "index.html") -> str:
    """Write HTML content to a file in the output folder.
    
    This tool creates beautiful HTML files with proper formatting and saves them 
    to the output directory for easy access and viewing.
    
    Args:
        html_content: The complete HTML content to write to the file, including DOCTYPE, head, and body sections
        filename: The name of the HTML file to create (defaults to 'index.html')
    
    Returns:
        A confirmation message indicating the file was successfully written
    """
    # Create output directory in the same directory as the main script
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(script_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    # Ensure filename has .html extension
    if not filename.endswith('.html'):
        filename += '.html'
    
    # Write HTML to file
    file_path = os.path.join(output_dir, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    return f"HTML successfully written to {file_path}" 