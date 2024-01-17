variable "project" {
    description = "Project"
    default = "dtc-de-zoomcamp-411514"
}

variable "location" {
    description = "Project Location"
    default = "EU"
}

variable "region" {
    description = "Project Region"
    default = "europe-west-2"
}

variable "bq_dataset_name" {
    description = "My BigQuery dataset name"
    default = "demo_dataset"
}

variable "gcs_bucket_name" {
    description = "Storage Bucket Name"
    default = "dtc-de-zoomcamp-411514-terra-bucket"
}

variable "gcs_storage_class" {
    description = "Bucket Storage Class"
    default = "STANDARD"
}