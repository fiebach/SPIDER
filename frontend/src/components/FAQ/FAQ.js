import React from 'react';
import { Layout } from 'antd';
import NavigationBar from "../NavigationBar/NavigationBar";
import styled from 'styled-components';
import Database from '../Database/Database';
const { Content } = Layout;

const Container = styled.div`
  padding: 50px 50px;
  max-width: 60%;
`;
/**
 * Includes the content for the FAQ page
 */

const FAQ = () => {
  return (
    <Layout>
      <NavigationBar />
      <Content>
        <Container>
          <h2 style={{ fontWeight: 'bold', textAlign: 'left' }}>Welcome to SPIDER - the System for Protein, Interactions, Drugs, and Exploratory Research!</h2>
          <p>Our platform provides an immersive experience for exploring and analyzing a segment of the ProCan dataset. With a primary focus on identifying associated proteins and drugs for individual or groups of proteins, SPIDER offers comprehensive tools for in-depth research.</p>
          <br/>
          <h2 style={{ fontWeight: 'bold', textAlign: 'left' }}>Frequently Asked Questions</h2>
          <h1 style={{ fontWeight: 'bold', textAlign: 'left' }}>1. How can i select or deselect a node?</h1>
          <p>You can select or deselect a node by double-clicking on it. A selected node will be outlined in yellow. On the left side, you'll find the Node Selection panel, where you can view all selected nodes and choose to select or deselect groups of nodes as well.</p>
          <br/>
          <h1 style={{ fontWeight: 'bold', textAlign: 'left' }}>2. What are the Minimum and Maximum Beta Values for ASSOCIATION Relationships?</h1>
          <p>The minimum Beta value is -1.950, while the maximum Beta value is 2.573.</p>
          <br/>         
          <h1 style={{ fontWeight: 'bold', textAlign: 'left' }}>2. What is the difference between LOW CONFIDENCE and HIGH CONFIDENCE Relationships between proteins and cell lines?</h1>
          <p>- LOW CONFIDENCE: Proteomics data for the entire set of 8498 quantified proteins at the cell line level, averaged across all the replicates.</p>
          <p>- HIGH CONFIDENCE: Proteomics data for 6692 proteins supported by measuring more than one peptide at the cell line level, averaged across all the replicates.</p>
          <br/>
          <h2 style={{ fontWeight: 'bold', textAlign: 'left' }}>Tutorial</h2>
          In this tutorial video, we'll guide you through using SPIDER.
          <iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ?si=8N73JwR8m7FjazkY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
           <br/>
           <h1 style={{ fontWeight: 'bold', textAlign: 'left' }}>Overview over the database sources</h1>
            <Database/>
           <br/>
          <h1 style={{ fontWeight: 'bold', textAlign: 'left' }}>Licenses used on this website</h1>
          <ul style={{ listStyleType: 'disc' }}>
              <li>DrugBank under Creative Common's Attribution-NonCommercial 4.0 International License. <a href="https://go.drugbank.com/releases/latest">Link to download</a></li>
              <li>Cell Line node picture: Image of a biology cancer cell, obtained from Iconduck and licensed under CC BY 3.0. <a href="https://iconduck.com/illustrations/122610/biology-cancer-cell-disease-health-human-tumor">Link to image</a></li>
              <li>Spider picture: Modified image of bug spider 2, sourced from Iconduck and licensed under CC0. <a href="https://iconduck.com/icons/250210/bug-spider-2">Link to image</a></li>
          </ul>
        </Container>
      </Content>
    </Layout>
  );
};

export default FAQ;
