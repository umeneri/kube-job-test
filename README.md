# quick start

gcloud components install kubectl

gcloud init
> set default region

gcloud container clusters create mycluster
gcloud container clusters get-credentials mycluster
kubectl run hello-server --image gcr.io/google-samples/hello-app:1.0 --port 8080

Deployment → デプロイの単位の用に思える


kubectl expose deployment hello-server --type LoadBalancer \
  --port 80 --target-port 8080

curl http://[EXTERNAL_IP]
kubectl delete service hello-server
gcloud container clusters delete mycluster

# deploy web application
Pod: container or titly-coupled container gloup

# gke job
[GKEを使ったバッチジョブ実行 - DRYな備忘録](http://otiai10.hatenablog.com/entry/2017/12/19/162430)
https://cloud.google.com/kubernetes-engine/docs/how-to/jobs

controller object ∋ Job

Jobはバッチ用podの管理者みたいなもの。
podがバッチ処理成功したらカウントしていって、所望のカウント数までバッチしたら処理終了する。
podが途中で落ちても新しいpodを呼ぶ。マネジャーみたいなものか。


実行：
kubectl apply -f config.yaml

状況確認：
kubectl describe job/example-job

標準出力：
kubectl logs example-job-2-m9sc5


build:
docker build -t gcr.io/gcpdev/gcs-py .
gcloud docker -- push gcr.io/gcpdev/gcs-py

create key:
kubectl create secret generic gcs-key --from-file==gcs.json

delete key:
kubectl delete secret gcs-key

cron:
[Running Automated Tasks with a CronJob - Kubernetes](https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/)


# 疑問点
> - シークレットな環境変数や値をどうやってもたせるか
> - 環境変数の設定方法 → Dockerfileで
- NATの設定をどうするか
- セキュリティグループに相当する機能は
- IAMに相当する機能は？
- データ永続化方法は

# tutorialすべて
https://cloud.google.com/kubernetes-engine/docs/tutorials/

# gsutilの権限 https://stackoverflow.com/a/33902486/5229454

credentialはenvで指定
https://cloud.google.com/docs/authentication/getting-started

[GKEでkubernetesベースのシンプルなバッチを動かす - Qiita](https://qiita.com/koduki/items/5b3a0471140f0b3b16a5)

# stackdriver logging
1. API有効化:
- https://console.developers.google.com/apis/library/logging.googleapis.com?project=gcpdev
- https://console.developers.google.com/apis/api/monitoring.googleapis.com/landing?project=gcpdev

2.
create clusterでデフォルトだと有効化されている

3. visit viewer
https://console.cloud.google.com/logs/viewer?_ga=2.101066625.-1446685781.1544019627&project=gcpdev&folder&organizationId&minLogLevel=0&expandAll=false&timestamp=2019-03-24T09:20:39.565000000Z&customFacets=&limitCustomFacetWidth=true&interval=NO_LIMIT&resource=container%2Fcluster_name%2Fmycluster&scrollTimestamp=2019-03-24T04:06:19.857928765Z

4. quering:
https://cloud.google.com/monitoring/kubernetes-engine/legacy-stackdriver/logging
use advanced filter

basic:
https://cloud.google.com/logging/docs/view/basic-filters


# python sample
[python-docs-samples/snippets.py at master · GoogleCloudPlatform/python-docs-samples](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/auth/cloud-client/snippets.py)


# dockerでpip installをキャッシュする
https://medium.com/@aidobreen/using-docker-dont-forget-to-use-build-caching-6e2b4f43771e


