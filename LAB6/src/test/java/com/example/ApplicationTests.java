package com.example;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.web.servlet.MockMvc;
import java.util.List;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(PointsController.class)
public class ApplicationTests {
    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private PointsService pointsService;

    @Autowired
    private ObjectMapper objectMapper;

    @Test
    public void getListReturnListOfPoints() throws Exception {
        when(pointsService.getPoints()).thenReturn(List.of(
                new Points(1, 2),
                new Points(3, 4))
        );
        mockMvc.perform(get("/"))
                .andExpect(status().isOk())
                .andExpect(content().json("[{\"x\":1,\"y\":2},{\"x\":3,\"y\":4}]"));
    }

    @Test
    public void getNPointsReturnNPoints() throws Exception {
        final int n = 3;
        when(pointsService.getPointsByN(n)).thenReturn(List.of(
                new Points(1, 2),
                new Points(3, 4),
                new Points(5, 6))
        );

        mockMvc.perform(get("/" + n))
                .andExpect(status().isOk())
                .andExpect(content().string(objectMapper.writeValueAsString(List.of(
                        new Points(1, 2),
                        new Points(3, 4),
                        new Points(5, 6))
                )));
    }

    //Nie wiem dlaczego ten test na dystans nie przechodzi
    @Test
    public void getDistanceReturnDistance() throws Exception {
        final int x1 = 10;
        final int y1 = 20;
        final int x2 = 30;
        final int y2 = 40;
        final double distance = 0.0;

        when(pointsService.getDistance(new Points(x1, y1), new Points(x2, y2))).thenReturn(distance);

        mockMvc.perform(get("/distance/" + x1 + "/" + y1 + "/" + x2 + "/" + y2))
                .andExpect(status().isOk())
                .andExpect(content().string(String.valueOf(distance)));
    }

    @Test
    public void postPointReturnPoint() throws Exception {
        final Points point = new Points(1, 2);
        when(pointsService.addPoints(point)).thenReturn(true);

        mockMvc.perform(post("/add/{x}/{y}", point.getX(), point.getY())
                .content(objectMapper.writeValueAsString(point)))
                .andExpect(status().isOk())
                .andReturn();
    }

    @Test
    public void deletePointReturnPoint() throws Exception {
        final int point = 0;
        when(pointsService.deletePoints(point)).thenReturn(new Points(1, 2));

        mockMvc.perform(delete("/delete/{id}", 0))
                .andExpect(status().isOk())
                .andExpect(content().json("{\"x\":1,\"y\":2}"));
    }
}