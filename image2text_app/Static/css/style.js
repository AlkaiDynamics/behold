import { StyleSheet } from 'react-native';

export default StyleSheet.create({
  body: {
    fontFamily: 'Montserrat, sans-serif',
    margin: 0,
    padding: 0,
    background: 'linear-gradient(45deg, #6D83F2, #A8BDFE)',
    color: '#fff',
  },
  container: {
    width: '90%',
    margin: 'auto',
    overflow: 'hidden',
  },
  header: {
    background: '#333',
    color: '#fff',
    padding: 20,
    borderBottom: '3px solid #444',
    boxShadow: '0 2px 5px rgba(0, 0, 0, 0.3)',
  },
  headerTitle: {
    padding: 20,
  },
  navList: {
    padding: 0,
    listStyle: 'none',
    display: 'flex',
  },
  navItem: {
    marginRight: 20,
  },
  navLink: {
    textDecoration: 'none',
    color: '#fff',
    fontWeight: 'bold',
    transition: 'color 0.3s ease',
  },
  navLinkHover: {
    color: '#a8bdfd',
  },
  form: {
    background: 'rgba(255, 255, 255, 0.9)',
    padding: 20,
    borderRadius: 8,
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
    marginTop: 20,
  },
  button: {
    background: '#2196F3',
    color: 'white',
    padding: 10,
    border: 'none',
    borderRadius: 4,
    cursor: 'pointer',
    transition: 'background 0.3s ease',
  },
  buttonHover: {
    background: '#1E88E5',
  },
  resultBox: {
    background: 'rgba(255, 255, 255, 0.9)',
    padding: 20,
    marginTop: 20,
    borderRadius: 8,
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
    fontSize: 1.1,
    lineHeight: 1.6,
    wordBreak: 'break-word',
  },
  messages: {
    padding: 10,
    marginBottom: 20,
    border: '1px solid transparent',
    borderRadius: 4,
    color: '#a94442',
    backgroundColor: '#f2dede',
    borderColor: '#ebccd1',
    textAlign: 'center',
  },
  footer: {
    textAlign: 'center',
    padding: 20,
    borderTop: '1px solid #e1e1e1',
    marginTop: 50,
  },
});
