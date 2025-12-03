import json

class FMS_FileLoader:
    """Load and return contents of various file types."""
    
    def __init__(self, encoding: str = 'utf-8'):
        """
        Initialize FileLoader.
        
        Args:
            encoding: File encoding (default: utf-8)
        """
        self.encoding = encoding
    
    def load_file(self, file_path: str) -> str:
        """
        Load and return file contents as string.
        
        Args:
            file_path: Path to the file
                
        Returns:
            File contents as string
                
        Raises:
            FileNotFoundError: If file does not exist
            IOError: If file cannot be read
        """
        try:
            with open(file_path, 'r', encoding=self.encoding) as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found")
            raise
        except IOError as e:
            print(f"Error reading file: {e}")
            raise
    
    def load_file_lines(self, file_path: str) -> list:
        """
        Load file and return contents as list of lines.
        
        Args:
            file_path: Path to the file
                
        Returns:
            List of file lines
        """
        with open(file_path, 'r', encoding=self.encoding) as f:
            return f.readlines()
    
    def load_python_file(self, file_path: str) -> str:
        """
        Load and return the contents of a Python file.
        
        Args:
            file_path: Path to the Python file
                
        Returns:
            The file contents as a string
        """
        return self.load_file(file_path)
    
    def load_python_file_lines(self, file_path: str) -> list:
        """
        Load a Python file and return contents as a list of lines.
        
        Args:
            file_path: Path to the Python file
                
        Returns:
            List of file lines
        """
        return self.load_file_lines(file_path)


file_loader_instance = FMS_FileLoader()

def callback(ch, method, properties, body):
    message = json.loads(body)              #message
    print(f"[FMS] Received message: {message}")
    file_path = message.get('file_path')
    print(f"[FMS] Received request to load file: {file_path}")
    try:
        file_contents = file_loader_instance.load_file(file_path)
        print(f"[FMS] File loaded successfully. Contents length: {len(file_contents)} characters.")
        # Here you can add code to process the file contents as needed
    except Exception as e:
        print(f"[FMS] Error loading file: {e}")
        ch.basic_ack(delivery_tag=method.delivery_tag)  
        return
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f"[FMS] Acknowledged message for file: {file_path}")
    