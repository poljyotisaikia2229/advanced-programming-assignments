// App.js

import React, { useState } from 'react';
import {
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';

const App = () => {
  // Counter State
  const [counterValue, setCounterValue] = useState(0);

  // Theme State
  const [isDarkMode, setIsDarkMode] = useState(false);

  // Theme Colors
  const theme = {
    backgroundColor: isDarkMode ? '#121212' : '#FFFFFF',
    textColor: isDarkMode ? '#FFFFFF' : '#121212',
    buttonBackground: isDarkMode ? '#1E88E5' : '#1976D2',
    secondaryButton: isDarkMode ? '#424242' : '#E0E0E0',
    secondaryButtonText: isDarkMode ? '#FFFFFF' : '#121212',
  };

  // Increment Counter
  const handleIncrement = () => {
    setCounterValue((previousValue) => previousValue + 1);
  };

  // Decrement Counter with Guardrail
  const handleDecrement = () => {
    if (counterValue > 0) {
      setCounterValue((previousValue) => previousValue - 1);
    }
  };

  // Reset Counter
  const handleReset = () => {
    setCounterValue(0);
  };

  // Toggle Theme
  const toggleTheme = () => {
    setIsDarkMode((previousMode) => !previousMode);
  };

  return (
    <View
      style={[
        styles.container,
        { backgroundColor: theme.backgroundColor },
      ]}
    >
      <StatusBar
        barStyle={isDarkMode ? 'light-content' : 'dark-content'}
        backgroundColor={theme.backgroundColor}
      />

      {/* App Title */}
      <Text style={[styles.titleText, { color: theme.textColor }]}>
        Simple Digital Counter
      </Text>

      {/* Counter Display */}
      <View style={styles.counterContainer}>
        <Text style={[styles.counterText, { color: theme.textColor }]}>
          {counterValue}
        </Text>
      </View>

      {/* Increment / Decrement Buttons */}
      <View style={styles.buttonRow}>
        <TouchableOpacity
          style={[
            styles.actionButton,
            { backgroundColor: theme.secondaryButton },
          ]}
          onPress={handleDecrement}
          activeOpacity={0.8}
        >
          <Text
            style={[
              styles.buttonText,
              { color: theme.secondaryButtonText },
            ]}
          >
            -
          </Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[
            styles.actionButton,
            { backgroundColor: theme.buttonBackground },
          ]}
          onPress={handleIncrement}
          activeOpacity={0.8}
        >
          <Text style={styles.buttonText}>+</Text>
        </TouchableOpacity>
      </View>

      {/* Reset Button */}
      <TouchableOpacity
        style={[
          styles.resetButton,
          { backgroundColor: theme.secondaryButton },
        ]}
        onPress={handleReset}
        activeOpacity={0.8}
      >
        <Text
          style={[
            styles.resetButtonText,
            { color: theme.secondaryButtonText },
          ]}
        >
          Reset Counter
        </Text>
      </TouchableOpacity>

      {/* Theme Toggle Button */}
      <TouchableOpacity
        style={[
          styles.themeButton,
          { backgroundColor: theme.buttonBackground },
        ]}
        onPress={toggleTheme}
        activeOpacity={0.8}
      >
        <Text style={styles.buttonText}>
          Switch to {isDarkMode ? 'Light' : 'Dark'} Mode
        </Text>
      </TouchableOpacity>
    </View>
  );
};

export default App;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 20,
  },

  titleText: {
    fontSize: 28,
    fontWeight: '700',
    marginBottom: 40,
    textAlign: 'center',
  },

  counterContainer: {
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 50,
  },

  counterText: {
    fontSize: 80,
    fontWeight: 'bold',
  },

  buttonRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: '80%',
    marginBottom: 25,
  },

  actionButton: {
    width: 120,
    height: 60,
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
    elevation: 3,
  },

  buttonText: {
    color: '#FFFFFF',
    fontSize: 24,
    fontWeight: 'bold',
  },

  resetButton: {
    width: '80%',
    height: 55,
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 20,
    elevation: 2,
  },

  resetButtonText: {
    fontSize: 18,
    fontWeight: '600',
  },

  themeButton: {
    width: '80%',
    height: 55,
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
    elevation: 2,
  },
});