/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.ndl.services;

import com.ndl.fxenglishapp.PrimaryController;
import com.ndl.pojo.Choice;
import com.ndl.pojo.JdbcUtils;
import com.ndl.pojo.Question;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author admin
 */
public class QuestionServices {
    public List<Question> getQuestions(int num) throws SQLException {
        List<Question> questions = new ArrayList<>();
        try (Connection conn = JdbcUtils.getConn()) {
            PreparedStatement stm = conn.prepareCall("SELECT * FROM question ORDER BY rand() LIMIT ?");
            stm.setInt(1, num);
            
            ResultSet rs = stm.executeQuery();
            while(rs.next()) {
                Question q = new Question(rs.getString("id"), rs.getString("content"), rs.getInt("category_id"));
                questions.add(q);
            }
        } catch(SQLException ex) {
            Logger.getLogger(PrimaryController.class.getName()).log(Level.SEVERE, null, ex);
        }
        return questions;
    }
    
    public List<Choice> getChoices(String questionId) throws SQLException {
        List<Choice> choices = new ArrayList<>();
        try (Connection conn = JdbcUtils.getConn()) {
            PreparedStatement stm = conn.prepareCall("SELECT * FROM choice WHERE question_id = ?");
            stm.setString(1, questionId);
            
            ResultSet rs = stm.executeQuery();
            while(rs.next()) {
                Choice c = new Choice(rs.getString("id"), rs.getString("content"), rs.getBoolean("is_correct"), rs.getString("question_id"));
                choices.add(c);
            }
        } catch(SQLException ex) {
            Logger.getLogger(PrimaryController.class.getName()).log(Level.SEVERE, null, ex);
        }
        return choices;
    }
}
