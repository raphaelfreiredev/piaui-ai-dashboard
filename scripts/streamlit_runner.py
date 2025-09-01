"""
Helper script to run the Streamlit app with proper configuration
"""
import subprocess
import sys
import os

def run_streamlit():
    """Run the Streamlit application"""
    
    # Ensure we're in the right directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    os.chdir(project_dir)
    
    # Run streamlit
    cmd = [
        sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
        "--server.port", "8501",
        "--server.address", "localhost",
        "--browser.gatherUsageStats", "false"
    ]
    
    print("Starting Streamlit dashboard...")
    print("Dashboard will be available at: http://localhost:8501")
    print("Press Ctrl+C to stop the server")
    
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\nStreamlit server stopped.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit: {e}")

if __name__ == "__main__":
    run_streamlit()
