FROM golang:alpine
WORKDIR /usr/src/app
ADD ./hello.go /usr/src/app
RUN go build -o hello hello.go
CMD ["./hello"]
