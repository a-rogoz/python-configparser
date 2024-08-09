import configparser


config = configparser.ConfigParser()

config_dict = {
    "DEFAULT": {
        "host": "localhost"
    },
    "mariadb": {
        "name": "hello",
        "user": "root",
        "password": "password"
    },
    "redis": {
        "port": 6379,
        "db": 0
    }
}

config.read_dict(config_dict)
# read_file, read_string
# print(config.read("config.ini"))

print("Sections:", config.sections(), "\n")

print("mariadb section:")
print("Host:", config["mariadb"]["host"])
print("Host:", config.get("mariadb", "host"))
print("Databse:", config["mariadb"]["name"])
print("Username", config["mariadb"]["user"])
print("Password", config["mariadb"]["password"], "\n")

print("redis section:")
print("Host:", config["redis"]["host"])
print("Port", config["redis"]["port"])
print("Database number:", int(config["redis"]["db"]))

config["redis"]["db"] = "1"

with open("config.ini", "w") as configfile:
    config.write(configfile)


#####


exported_config = configparser.ConfigParser()

exported_config["DEFAULT"] = {"host": "localhost"}
exported_config["mariadb"] = {"name": "hello",
                              "user": "root",
                              "password": "password"}
exported_config["redis"] = {"port": 6379,
                            "db": 0}

with open("settings.ini", "w") as configfile:
    exported_config.write(configfile)


#####


config = configparser.ConfigParser()
config.read("mess.ini")  # Available in the Lab's working directory

# Dev config.
dev_config = configparser.ConfigParser()
# Prod config.
prod_config = configparser.ConfigParser()

# MariaDB
mariadb_env = config.get("mariadb", "env")

if mariadb_env == "dev":
    config["mariadb"].pop("env")
    dev_config["mariadb"] = config["mariadb"]
    
if mariadb_env == "prod":
    config["mariadb"].pop("env")
    prod_config["mariadb"] = config["mariadb"]

# Sentry
sentry_env = config.get("sentry", "env")

if sentry_env == "dev":
    config["sentry"].pop("env")
    dev_config["sentry"] = config["sentry"]
    
if sentry_env == "prod":
    config["sentry"].pop("env")
    prod_config["sentry"] = config["sentry"]

# Redis
redis_env = config.get("redis", "env")

if redis_env == "dev":
    config["redis"].pop("env")
    dev_config["redis"] = config["redis"]
    
if redis_env == "prod":
    config["redis"].pop("env")
    prod_config["redis"] = config["redis"]

# GitHub
github_env = config.get("github", "env")

if github_env == "dev":
    config["github"].pop("env")
    dev_config["github"] = config["github"]
    
if github_env == "prod":
    config["github"].pop("env")
    prod_config["github"] = config["github"]

# Prod
print("[sentry]")
for key, value in prod_config["sentry"].items():
    print(f"{key}={value}")

print()

print("[github]")
for key, value in prod_config["github"].items():
    print(f"{key}={value}")

print("-----")

# Dev
print("[mariadb]")
for key, value in dev_config["mariadb"].items():
    print(f"{key}={value}")

print()

print("[redis]")
for key, value in dev_config["redis"].items():
    print(f"{key}={value}")

with open("dev_config.ini", mode="w") as configfile:
    dev_config.write(configfile)

with open("prod_config.ini", mode="w") as configfile:
    prod_config.write(configfile)