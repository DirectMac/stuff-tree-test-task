FROM node:lts AS development

RUN npm install -g pnpm

WORKDIR /app/client
COPY package.json .
COPY pnpm-lock.yaml .
RUN pnpm install
COPY . /app/client
