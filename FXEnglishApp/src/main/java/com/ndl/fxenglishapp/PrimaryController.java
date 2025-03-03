package com.ndl.fxenglishapp;

import com.ndl.pojo.Question;
import com.ndl.services.QuestionServices;
import java.io.IOException;
import java.net.URL;
import java.sql.SQLException;
import java.util.List;
import java.util.ResourceBundle;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;
import javafx.scene.control.RadioButton;
import javafx.scene.text.Text;

public class PrimaryController implements Initializable {
    @FXML private Text textContent;
    @FXML private RadioButton rdoA;
    @FXML private RadioButton rdoB;
    @FXML private RadioButton rdoC;
    @FXML private RadioButton rdoD;
    private List<Question> question;
    private int currentId = 0;
    private List<Question> questions;
    @FXML private Text textA;
    @FXML private Text textB;
    @FXML private Text textC;
    @FXML private Text textD;
    
    @FXML
    private void switchToSecondary() throws IOException {
        App.setRoot("secondary");
    }
    
    public void checkHandler(ActionEvent e) throws SQLException {
        QuestionServices s = new QuestionServices();
        List<Question> questions = s.getQuestions(2);
        
        Alert a = new Alert(Alert.AlertType.INFORMATION, questions.get(0).getContent(), ButtonType.OK);
        a.show();
    }

    @Override
    public void initialize(URL url, ResourceBundle rb) {
        QuestionServices s = new QuestionServices();
        try {
            this.questions = s.getQuestions(3);
            loadQuestionToUI();
        } catch (SQLException ex) {
            Logger.getLogger(PrimaryController.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    private void loadQuestionToUI() throws SQLException {
        QuestionServices s = new QuestionServices();
        Question q = this.questions.get(currentId);
        textContent.setText(q.getContent());
        
        if(q.getChoices() == null) {
            try {
                q.setChoices(s.getChoices(q.getId()));
                textA.setText(q.getChoices().get(0).toString());
            } catch (SQLException ex) {
            Logger.getLogger(PrimaryController.class.getName()).log(Level.SEVERE, null, ex);
        }
        }
    }
}
