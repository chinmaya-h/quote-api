package com.example.quoteapi;

import java.util.List;
import java.util.Map;
import java.util.concurrent.ThreadLocalRandom;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class QuoteController {
    private final List<String> quotes = List.of(
        "It always seems impossible until it's done.",
        "Great things are done by a series of small things brought together.",
        "The secret of getting ahead is getting started."
    );

    @GetMapping("/")
    public Map<String, String> home() {
        return Map.of("app", "Quote API", "status", "running");
    }

    @GetMapping("/quote")
    public Map<String, String> randomQuote() {
        int index = ThreadLocalRandom.current().nextInt(quotes.size());
        return Map.of("quote", quotes.get(index));
    }

    @GetMapping("/quotes")
    public List<String> allQuotes() {
        return quotes;
    }

    @GetMapping("/health")
    public Map<String, String> health() {
        return Map.of("status", "UP");
    }
}
