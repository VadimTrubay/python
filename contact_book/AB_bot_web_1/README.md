1- Робимо білд імеджу!
 docker build . -t osandreyman/address_book_bot:0.0.1
2- Запуск контейнера з імеджу!
 docker run -it --name address_book_bot -v /Users/andriiosypenko/Desktop/FinalProject/data:/data osandreyman/address_book_bot:0.0.1
3- Для запуску нового контейнеру треба зупиеити та видалити старий контейнер. 
 docker stop address_book_bot:0.0.1 
docker rm restaurant  / docker rmi address_book_bot:0.0.1
4- Перевірити створені контейнери!
 docker ps -a
5- Завантаження імеджу до репозіторію на докер Хаб.
docker push osandreyman/address_book_bot:0.0.1
