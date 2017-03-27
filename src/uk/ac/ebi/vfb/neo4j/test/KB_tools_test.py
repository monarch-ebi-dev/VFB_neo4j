'''
Created on Mar 8, 2017

@author: davidos
'''
import unittest
from ..KB_tools import kb_owl_edge_writer, node_importer


class TestEdgeWriter(unittest.TestCase):


    def setUp(self):
        self.edge_writer = kb_owl_edge_writer('http://localhost:7474', 'neo4j', 'neo4j')
        s = []
        s.append("MERGE (i1:Individual { IRI : 'Aya' }) " \
            "MERGE (r1:Property { IRI : 'http://fu.bar/loves', label : 'loves' }) " \
            "MERGE (i2:Individual { IRI: 'Freddy' }) ")
        s.append("MERGE (i1:Individual { IRI : 'Aya' }) " \
            "MERGE (r1:Property { IRI : 'daughter_of' }) " \
            "MERGE (i2:Individual { IRI: 'David' }) ")
        s.append("MERGE (s:Class { IRI: 'Person' } ) ")
        s.append("MERGE (s:Class { IRI: 'Toy' } ) " )                
        self.edge_writer.nc.commit_list(s)
        pass


    def tearDown(self):
        # TODO - add some deletions here
        s = ["MATCH (i1:Individual { IRI : 'Aya' })-" \
       "[r1:Related { IRI : 'http://fu.bar/loves' }]->" \
       "(i2:Individual { IRI: 'Freddy' }) DELETE i1, r1, i2"]
        s.append("(r1:Property { IRI : 'http://fu.bar/loves'}) DELETE r1")       
        self.edge_writer.nc.commit_list(s)
        pass


    def test_add_fact(self):

        self.edge_writer.add_fact(s = 'Aya', r = 'http://fu.bar/loves', 
                                  o = 'Freddy', 
                                  edge_annotations = { 'fu' : "ba'r", 
                                                      'bin': ['bash', "ba'sh"],
                                                      'i' : 1,                                                                                          
                                                      'x' : True })
        assert self.edge_writer.check_proprties() == True
        self.edge_writer.commit() 
        assert self.edge_writer.test_edge_addition() == True  
        self.edge_writer.add_fact(s = 'Aya', r = 'loved', o = 'Freddy', edge_annotations = {} )
        self.edge_writer.commit()
        assert self.edge_writer.test_edge_addition() == False

        
        # Add test of added content?
        
        
    def test_add_anon_type_ax(self):
        pass
    
    def test_add_named_type_ax(self):
        self.edge_writer.add_named_type_ax(s = 'Aya', o = 'Person')
        self.edge_writer.commit()
        assert self.edge_writer.test_edge_addition() == True        
        r1 = self.edge_writer.nc.commit_list(["MATCH (i1:Individual { IRI : 'Aya' })-" \
        "[r1:Related { IRI : 'http://fu.bar/loves' }]->" \
        "(i2:Individual { IRI: 'Freddy' }) RETURN r1.label"])
        assert r1[0]['data'][0]['row'][0] == 'loves'
        
class TestNodeImporter(unittest.TestCase):

    def setUp(self):
        self.ni = node_importer('http://localhost:7474', 'neo4j', 'neo4j')
    
    def test_update_from_obograph(self):
#        self.ni.update_from_obograph(self, url = 'https://raw.githubusercontent.com/VirtualFlyBrain/VFB_owl/master/src/owl/vfb_ext.owl')
#        self.ni.commit()
#        test?
        pass
        

if __name__ == "__main__":
    unittest.main()
