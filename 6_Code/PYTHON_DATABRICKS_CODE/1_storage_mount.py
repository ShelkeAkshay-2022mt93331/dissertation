# Databricks notebook source
configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
}

try:
  dbutils.fs.mount(
    source = "abfss://bronze@storageaccmtechdemo.dfs.core.windows.net/",
    mount_point = "/mnt/bronze",
    extra_configs = configs)
  print("Mount Point created successfully")  
except:
  print("Mount Point already exists")  

# COMMAND ----------

dbutils.fs.ls("/mnt/bronze/SalesLT")

# COMMAND ----------

configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
}

try:
  dbutils.fs.mount(
    source = "abfss://silver@storageaccmtechdemo.dfs.core.windows.net/",
    mount_point = "/mnt/silver",
    extra_configs = configs)
  print("Mount Point created successfully")  
except:
  print("Mount Point already exists")  

# COMMAND ----------

configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
}

try:
  dbutils.fs.mount(
    source = "abfss://gold@storageaccmtechdemo.dfs.core.windows.net/",
    mount_point = "/mnt/gold",
    extra_configs = configs)
  print("Mount Point created successfully")  
except:
  print("Mount Point already exists")  
