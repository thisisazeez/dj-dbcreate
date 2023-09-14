import subprocess

def check_postgres_installed():
    try:
        # Use the 'pg_isready' command to check if PostgreSQL is installed and running
        subprocess.run(
            "pg_isready", stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        return False
