// HelmSphereClient.java
// Demonstration of Java integration in the HelmSphere project
// This file simulates how Java could interact with the Flask-based backend
// to send helmet detection requests and receive responses.

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;

public class HelmSphereClient {
    public static void main(String[] args) {
        System.out.println("=== HelmSphere Java Client Simulation ===\n");

        try {
            // Simulated API endpoint of Flask backend
            String apiUrl = "http://127.0.0.1:5000/detect";

            // Normally, we would send the video file to the backend using POST
            System.out.println("Connecting to backend API at: " + apiUrl);
            System.out.println("Preparing video data (helmet.mp4) for detection...");

            // Simulated network delay
            Thread.sleep(1500);

            // Mock response to represent backend detection result
            System.out.println("Sending data to backend...");
            Thread.sleep(1500);
            System.out.println("Response received from server:");
            System.out.println("{ \"helmet_detected\": true }");

            System.out.println("\n✅ Java successfully communicated with Flask backend (simulation).");
        } 
        catch (InterruptedException e) {
            System.out.println("Simulation interrupted!");
        } 
        catch (Exception e) {
            System.out.println("An error occurred while simulating the request.");
        }

        System.out.println("\n--- End of Simulation ---");
    }
}
