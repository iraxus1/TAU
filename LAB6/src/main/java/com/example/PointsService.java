package com.example;

import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class PointsService {

    private List<Points> points = new ArrayList<>();

    public List<Points> getPoints() {
        return points;
    }

    public boolean addPoints(Points points) {
        return this.points.add(points);
    }

    public Points deletePoints(int index) {
        return this.points.remove(index);
    }

    public List<Points> getPointsByN(int n) {
        return this.points.subList(0, n);
    }

    public double getDistance(Points p1, Points p2) {
        return Math.sqrt(Math.pow(p1.getX() - p2.getX(), 2) + Math.pow(p1.getY() - p2.getY(), 2));
    }
}
