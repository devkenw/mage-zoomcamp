variable "credentials" {
  description = "service account secret key path"
  default     = "./de-mage-demo-eb378b1a5d8b.json"
}

variable "project" {
  description = "project"
  default     = "de-mage-demo"
}

variable "region" {
  description = "region"
  default     = "us-central1"
}

variable "bucket_name" {
  description = "storage bucket name"
  default     = "de_mage_demo_bucket"
}

variable "location" {
  description = "project location"
  default     = "US"
}

variable "bucket_storage_class" {
  description = "bucket storage class"
  default     = "STANDARD"
}

variable "bq_dataset_name" {
  description = "bigquery dataset name"
  default     = "ny_taxi"
}

