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
          <p>You can select or deselect a node by double-clicking on it. A selected node will be outlined in yellow. On the left side, you'll find the Node Selection panel, where you can view all selected nodes and choose to select or deselect groups of nodes as well. Also ypu can hold the Ctrl key and mark a area. All nodes in this area will be selected</p>
          <br/>
          <h1 style={{ fontWeight: 'bold', textAlign: 'left' }}>2. What are the Minimum and Maximum Beta Values for ASSOCIATION Relationships?</h1>
          <p>The minimum Beta value is -1.950, while the maximum Beta value is 2.573.</p>
          <br/>         
          <h1 style={{ fontWeight: 'bold', textAlign: 'left' }}>3. What is the difference between LOW CONFIDENCE and HIGH CONFIDENCE Relationships between proteins and cell lines?</h1>
          <p>- LOW CONFIDENCE: Proteomics data for the entire set of 8498 quantified proteins at the cell line level, averaged across all the replicates.</p>
          <p>- HIGH CONFIDENCE: Proteomics data for 6692 proteins supported by measuring more than one peptide at the cell line level, averaged across all the replicates.</p>
          <br/>
          <h1 style={{ fontWeight: 'bold', textAlign: 'left' }}>4. What do the Analysis Tools do?</h1>
<p><strong>- Find Connections:</strong> This tool allows you to discover connections from one or more selected nodes to other nodes that have a relationship with the selected nodes. You can specify criteria for the nodes and relationships that should be returned.</p>
<p><strong>- Shortest Path:</strong> When you select two nodes, this tool finds the shortest path between them in the network graph. You can also define which types of connections are allowed in the shortest path.</p>
<p><strong>- Explore PPI Neighborhood:</strong> This tool identifies proteins connected to a group of selected proteins based on their centrality in the BioGRID PPI network relative to the selected proteins. The algorithm is based on the code and documentation from Drugst.One. Note that differences between the implementation and database in Drugst.One and SPIDER may lead to varying results.</p>
<p><strong>- Find Nearest ProCan Protein:</strong> This tool identifies the closest ProCan Protein for proteins found in the BioGRID database but not in the ProCan database. It utilizes a shortest path algorithm. This function is crucial because our database primarily contains information on relationships involving ProCan Proteins with entities such as cell lines or drugs.</p>

<h1 style={{ fontWeight: 'bold', textAlign: 'left' }}>5. How is the drug similarity determined?</h1>
<p>To calculate the drug similarity, we use a method that is also used in <a href="https://github.com/iMammal/CytoCave">CytoCave</a>. The diagram shows a simplified representation of the individual steps. </p>
<h1 style={{ fontWeight: 'bold', textAlign: 'left' }}>5. What does ProCan mean?</h1>
<p>ProCan is the ACFR International Centre for the Proteome of Human Cancer. In their new study <a href="https://www.cell.com/cancer-cell/fulltext/S1535-6108(22)00274-4#sectitle0030">Pan-cancer proteomic map of 949 human cell lines</a> they have generated an extensive dataset. For SPIDER itself, we mostly use data from a <a href="https://www.dropbox.com/sh/0nemsahltwwstjp/AADb9f6b99K4z2XUPwsJf96Qa?dl=0&e=1">Dropbox</a> link they provided.</p>

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
