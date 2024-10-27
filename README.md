# Ansible
Чтобы ansible заработал, нужно чтобы на Debian 11 был создан пользователь ansible с паролем 123

Также этот пользователь должен иметь права sudo

/etc/sudoers

ansible ALL=(ALL:ALL) NOPASSWD: ALL

Также предворительно должен быть установлен ssh

# CI/CD

Сборка Docker контейнера

docker build -t flask .

docker run -d -p 8080:8080 flask

Перейдите на http://localhost:8080/


# Monitoring

Prometheus и Blackbox exporter обернуты в docker compose.

Для запуска нужна лишь одна команда:

docker compose up

Чтобы посмотреть метрики Prometheus и Blackbox exporter нужно перейти на localhost:9090 и localhost:9115 соответсвенно

