# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jariza-o <jariza-o@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/21 11:52:37 by jariza-o          #+#    #+#              #
#    Updated: 2024/10/22 12:10:07 by jariza-o         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

COMPOSE_EXEC := docker compose
COMPOSE_FILE := docker-compose.yml

all: up

up:
	$(COMPOSE_EXEC) -f $(COMPOSE_FILE) up -d --build

run:
	docker build -t server-image ./web
	docker run --name server --env-file .env -v ./web/service:/PokeAPI -d server-image

down:
	$(COMPOSE_EXEC) -f $(COMPOSE_FILE) down

dev:
	$(COMPOSE_EXEC) -f $(COMPOSE_FILE) up --build

clean:
	$(COMPOSE_EXEC) -f $(COMPOSE_FILE) down --volumes --rmi all

re: down up

.PHONY: all run up down re clean