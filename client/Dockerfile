FROM node:16-slim AS builder

WORKDIR /svelte-app

RUN npm cache clean --force

COPY package.json .

COPY pnpm-lock.yaml .

RUN npm install -g pnpm

RUN pnpm install

COPY . .

RUN pnpm build

EXPOSE 80 443

#########
# CADDY #
#########

FROM caddy:2.5.1

COPY Caddyfile /etc/caddy/Caddyfile

COPY --from=builder /svelte-app/build /srv

CMD ["caddy", "run"]

#########
# NGINX #
#########

# FROM nginx:1.23.0

# RUN rm /etc/nginx/conf.d/default.conf

# COPY --from=builder /svelte-app/nginx.conf /etc/nginx/conf.d/

# COPY --from=builder /svelte-app/build /usr/share/nginx/html

# CMD ["nginx", "-g", "daemon off;"]
