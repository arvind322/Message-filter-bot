package com.example.milkcalculator;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.*;

public class MainActivity extends Activity {

    EditText milkMorning, fatMorning, rateMorning;
    EditText milkEvening, fatEvening, rateEvening;
    TextView totalMorningText, totalEveningText, finalTotalText;

    double totalMorning = 0;
    double totalEvening = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        milkMorning = findViewById(R.id.milk_morning);
        fatMorning = findViewById(R.id.fat_morning);
        rateMorning = findViewById(R.id.rate_morning);

        milkEvening = findViewById(R.id.milk_evening);
        fatEvening = findViewById(R.id.fat_evening);
        rateEvening = findViewById(R.id.rate_evening);

        totalMorningText = findViewById(R.id.total_morning);
        totalEveningText = findViewById(R.id.total_evening);
        finalTotalText = findViewById(R.id.final_total);
    }

    public void calculateMorning(View v) {
        double milk = Double.parseDouble(milkMorning.getText().toString());
        double fat = Double.parseDouble(fatMorning.getText().toString());
        double rate = Double.parseDouble(rateMorning.getText().toString());
        totalMorning = milk * fat * rate;
        totalMorningText.setText("Morning Total: ₹" + totalMorning);
    }

    public void calculateEvening(View v) {
        double milk = Double.parseDouble(milkEvening.getText().toString());
        double fat = Double.parseDouble(fatEvening.getText().toString());
        double rate = Double.parseDouble(rateEvening.getText().toString());
        totalEvening = milk * fat * rate;
        totalEveningText.setText("Evening Total: ₹" + totalEvening);
    }

    public void calculateFinal(View v) {
        double total = totalMorning + totalEvening;
        finalTotalText.setText("Total: ₹" + total);
    }
}
