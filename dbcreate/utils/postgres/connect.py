import psycopg2
import typer
from yaspin import yaspin
from dbcreate.utils.checkpsql import check_postgres_installed

app = typer.Typer()

def connect_to_postgres(user='postgres', password='', host='localhost', port='5432'):
    if not check_postgres_installed():
        print("PostgreSQL is not installed on your system.")
        return None

    if not password:
        # password = typer.prompt("Enter the PostgreSQL password for the 'postgres' user: ")
        password: str = typer.Option(..., prompt=True)

    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.autocommit = True
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

@app.command()
def connect():
    with yaspin(text="Connecting to PostgreSQL...", color="yellow") as spinner:
        connection = connect_to_postgres()
        if connection:
            spinner.success("✅ Connected to PostgreSQL with the default 'postgres' user.")
        else:
            spinner.fail("💥 Failed to connect to PostgreSQL.")

if __name__ == "__main__":
    app()
