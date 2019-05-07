package main
import (
  "net/http"
  "strings"
)

var token = "loaderio-3c7cdedd29a59ff8714d4bf41f1c1870"
func sendToken(w http.ResponseWriter, r *http.Request) {
  w.Write([]byte(token))
}

func sayHello(w http.ResponseWriter, r *http.Request) {
  message := r.URL.Path
  message = strings.TrimPrefix(message, "/")
  message = "Hello " + message
  w.Write([]byte(message))
}

func main() {
  http.HandleFunc("/"+token+"/", sendToken)
  http.HandleFunc("/", sayHello)
  if err := http.ListenAndServe(":8080", nil); err != nil {
    panic(err)
  }
}
