FROM google/cloud-sdk

CMD echo "1, 2, 3" > test.csv \
    && gcloud auth activate-service-account --key-file=/var/secrets/google/gcs.json \
    && gsutil cp test.csv gs://dev-gke-batch/ \
    && gsutil ls -l gs://dev-gke-batch/
# CMD while :; do date; sleep 1; done

