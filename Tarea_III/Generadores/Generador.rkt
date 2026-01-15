#lang racket/base

(define (gen-randoms n max)
  (for/list ([i n])
    (+ (random max) 1)))

(define datos (gen-randoms 1000000 20))

(with-output-to-file "Muestras/muestra_racket_int.txt"
  (lambda ()
    (for ([x datos])
      (displayln x)))
  #:exists 'replace)