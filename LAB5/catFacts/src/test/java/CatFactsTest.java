
import org.example.CatFacts;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static org.mockito.Mockito.when;
public class CatFactsTest {
    CatFacts catFacts = org.mockito.Mockito.mock(CatFacts.class);

    String url = "https://cat-fact.herokuapp.com/facts";

    @Test
    public void testGetFact() {
        when(catFacts.getFact(url + "/5887e1d85c873e0011036889")).thenReturn(
                """
                        {
                          "status": {
                            "verified": true,
                            "feedback": "",
                            "sentCount": 1
                          },
                          "_id": "5887e1d85c873e0011036889",
                          "user": {
                            "name": {
                              "first": "Alex",
                              "last": "Wohlbruck"
                            },
                            "_id": "5a9ac18c7478810ea6c06381",
                            "photo": "https://lh3.googleusercontent.com/a/AGNmyxY_EdZOjakO5QCnVdDojXDjfu6xrx8on4HSb5DkEsU=s50"
                          },
                          "text": "Cats make about 100 different sounds. Dogs make only about 10.",
                          "__v": 0,
                          "source": "user",
                          "updatedAt": "2020-09-03T16:39:39.578Z",
                          "type": "cat",
                          "createdAt": "2018-01-15T21:20:00.003Z",
                          "deleted": false,
                          "used": true
                        }"""
        );
        String fact = catFacts.getFact(url + "/5887e1d85c873e0011036889");
        Assertions.assertEquals(fact, """
                {
                  "status": {
                    "verified": true,
                    "feedback": "",
                    "sentCount": 1
                  },
                  "_id": "5887e1d85c873e0011036889",
                  "user": {
                    "name": {
                      "first": "Alex",
                      "last": "Wohlbruck"
                    },
                    "_id": "5a9ac18c7478810ea6c06381",
                    "photo": "https://lh3.googleusercontent.com/a/AGNmyxY_EdZOjakO5QCnVdDojXDjfu6xrx8on4HSb5DkEsU=s50"
                  },
                  "text": "Cats make about 100 different sounds. Dogs make only about 10.",
                  "__v": 0,
                  "source": "user",
                  "updatedAt": "2020-09-03T16:39:39.578Z",
                  "type": "cat",
                  "createdAt": "2018-01-15T21:20:00.003Z",
                  "deleted": false,
                  "used": true
                }""");
    }

    

}
