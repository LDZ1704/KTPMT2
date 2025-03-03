module com.ndl.fxenglishapp {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;

    opens com.ndl.fxenglishapp to javafx.fxml;
    exports com.ndl.fxenglishapp;
}
