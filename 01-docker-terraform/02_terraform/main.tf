terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.12.0"
    }
  }
}

provider "google" {
    project     = "dtc-de-zoomcamp-411514"
    region      = "europe-west2"
}

resource "google_storage_bucket" "auto-expire" {
  name          = "dtc-de-zoomcamp-411514-terra-bucket"
  location      = "EU"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id                  = "demo_dataset"
  location                    = "EU"
  default_table_expiration_ms = 3600000
}

