# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Dockerfile                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jariza-o <jariza-o@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/21 15:59:52 by jariza-o          #+#    #+#              #
#    Updated: 2024/10/21 16:38:02 by jariza-o         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

FROM python:3.12-bookworm

WORKDIR /backend

RUN apt update

COPY conf /conf
COPY tools/utils.sh /utils.sh
RUN chmod +x /utils.sh

RUN pip install -r /conf/requirements.txt

ENTRYPOINT [ "sh", "/utils.sh" ]
CMD ["sh", "-c", "while :; do echo 'Infinite loop'; sleep 1; done"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]