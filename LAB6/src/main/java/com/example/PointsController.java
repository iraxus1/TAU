package com.example;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
public class PointsController {

    private final PointsService pointsService;

    @Autowired
    public PointsController(PointsService pointsService) {
        this.pointsService = pointsService;
    }

    @GetMapping("/")
    public ResponseEntity<?> getPoints() {
        return ResponseEntity.ok(pointsService.getPoints());
    }
    @GetMapping("/{n}")
    public ResponseEntity<?> getPointsByN(@PathVariable int n) {
        return ResponseEntity.ok(pointsService.getPointsByN(n));
    }

    @GetMapping("/distance/{x1}/{y1}/{x2}/{y2}")
    public ResponseEntity<?> getDistance(@PathVariable("x1") int x1, @PathVariable("y1") int y1, @PathVariable("x2") int x2, @PathVariable("y2") int y2) {
        return ResponseEntity.ok(pointsService.getDistance(new Points(x1, y1), new Points(x2, y2)));
    }

    @PostMapping("add/{x}/{y}")
    public ResponseEntity<?> addPoints(@PathVariable int x, @PathVariable int y) {
        pointsService.addPoints(new Points(x, y));
        return ResponseEntity.ok(pointsService.getPoints());
    }

    @DeleteMapping("/delete/{id}")
    public ResponseEntity<?> deletePoints(@PathVariable int id) {
        return ResponseEntity.ok(pointsService.deletePoints(id));
    }
}
