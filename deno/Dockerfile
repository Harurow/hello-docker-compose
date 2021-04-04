FROM hayd/alpine-deno:latest
WORKDIR /app
USER deno
COPY . .
RUN deno cache app.ts
EXPOSE 3000
CMD ["run", "--allow-net", "--allow-env", "app.ts"]
